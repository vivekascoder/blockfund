import smartpy as sp


class SocialBlock(sp.Contract):
  def __init__(self):
    self.add_flag("initial-cast")
    self.init(
      causes=sp.big_map(
        tkey=sp.TNat, 
        tvalue=sp.TRecord(
          owner=sp.TAddress, 
          cause_title=sp.TString,
          balance=sp.TMutez
        )
      ),
      fundings=sp.big_map(
        tkey=sp.TRecord(
          cause_id=sp.TNat,
          funder=sp.TAddress
        ),
        tvalue=sp.TMutez
      )
    )

  @sp.entry_point
  def create_cause(self, cause_id, title):
    """ Creates a new cause. """
    # Verify if the cause_id doesn't exists
    sp.verify(~ self.data.causes.contains(cause_id))
    self.data.causes[cause_id] = sp.record(owner=sp.sender, cause_title=title , balance=sp.mutez(0))
  
  @sp.entry_point
  def fund_cause(self, cause_id):
    """ Funds a specific cause """
    # Verify if the cause_id exists
    sp.verify(self.data.causes.contains(cause_id))
    self.data.fundings[sp.record(cause_id=cause_id, funder=sp.sender)] = sp.amount
    self.data.causes[cause_id].balance += sp.amount
  
  @sp.entry_point
  def withdraw_funds(self, cause_id):
    """ It allows the owner of a cause to transfer withdraw the funds. """
    # Verify if the cause_id exists
    sp.verify(self.data.causes.contains(cause_id))
    # Verify if the sender/reciever is the owner of the cause
    sp.verify(self.data.causes[cause_id].owner == sp.sender)
    # Transfer the collected funds
    sp.send(self.data.causes[cause_id].owner, self.data.causes[cause_id].balance)
    # Reset the amount as it's withdrawn now.
    self.data.causes[cause_id].balance = sp.mutez(0)


@sp.add_test("Social Block")
def test():
  """ Test for our smart contract. """
  scenario = sp.test_scenario()
  social = SocialBlock()
  
  owner = sp.test_account("Owner")
  funder1 = sp.test_account("Funder1")
  funder2 = sp.test_account("Funder2")

  scenario += social
  scenario += social.create_cause(cause_id=1, title="Test").run(sender=owner)
  
  # Let's fund the cause
  scenario += social.fund_cause(1).run(sender=funder1, amount=sp.mutez(1000000))
  scenario += social.fund_cause(1).run(sender=funder2, amount=sp.mutez(2000000))
  
  # Let's verify the amount
  scenario.verify(social.data.causes[1].balance == sp.mutez(3000000))
  
  # Should raise an error
  scenario += social.create_cause(cause_id=1, title="Another Test").run(sender=owner, valid=False)
  
  # Withdrawing funds 
  # Should raise error 
  scenario += social.withdraw_funds(1).run(sender=funder1, valid=False)
  # scenario += social.create_cause(cause_id=2, title="Test").run(sender=owner)
  
  # With correct owner
  scenario += social.withdraw_funds(1).run(sender=owner)
  