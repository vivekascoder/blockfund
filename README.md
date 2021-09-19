<h1 align="center">
BlockFund
</h1>
<p align="center">
Raise crypto for social causes, and make a better future.
</p>

## 🦾 Table of Contents
- [🦾 Table of Contents](#-table-of-contents)
- [💚 What is BlockFund ?](#-what-is-blockfund-)
- [❔ How does it work ?](#-how-does-it-work-)
- [Presentaion (PPT)](#presentaion-ppt)
- [🛠️ Tools Used](#️-tools-used)
  - [💄 Frontend](#-frontend)
  - [📦️ Backend / Blockchain](#️-backend--blockchain)
  - [🌍 Deployment](#-deployment)
- [〽️ Problem It solves.](#️-problem-it-solves)
- [🦾 Challenges Faced](#-challenges-faced)
  - [🔍 Project Searching Face](#-project-searching-face)
  - [👨🏾‍💻 During the Development](#-during-the-development)
  - [🌐 During Deployment.](#-during-deployment)
- [🔥 Future Development](#-future-development)
- [☎️ Let's Connect](#️-lets-connect)

## 💚 What is BlockFund ?
Blockfund is a Decentralized FundRaising Platform for social causes. It's build on top of `Tezos` Blockchain. It aims to deliver better results for funding the social causes and saving the world.
**Live Url**: https://blockfund.biz

## ❔ How does it work ?
- **Step 1:** A organization or a person can create a cause for which he/she wants to raise funds for. 
- **Step 2:** Then other people who wants to donate to that cause can send the XTZ from there wallet.
- **Step 3:** Then the owner (Only Owner) who created the cause can withdraw the funds.

## Presentaion (PPT)
- Link: https://docs.google.com/presentation/d/1WCpCja077epZIomLPrFGimFfzQ3mLUDslD2Zij5fxvw/edit?usp=sharing

## 🛠️ Tools Used
![](./src/assets/BlockFund.png)

### 💄 Frontend
Frontend of BlockFund is written in Vuejs along with Quasar as a Component library to quickly build the frontend. I absolutely love 💚 VueJs and it's ecosystem and Quasar is one of the best UI Library to pick.

### 📦️ Backend / Blockchain
Since it's a decentralized aplication there is no bacend though you can find the smart contract which handles every thing at `./src/contract.py`.

The following `SmartPy` Code represents how and what data is stored on the blockchain.
```python
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
```

### 🌍 Deployment
It uses `Linode` cloud to host the web application using `Nginx` server. For SSL certificates i've used certbot.

## 〽️ Problem It solves.
This is the time when Web3.0 is booming and along with it the craze and the usecases of Blockchain based technologies is going to be the new present, the amount of people invesiting on crypto currencies are also rising specially in india. But we are also going through a lot of Natural Crises like `Covid19`, `WhiteFungus`, `BlackFungus`, Insufficient amount of Oxygen cylinders which causes a lot of deaths in India. Theese are the kind of causes my product `BlockFund` is targeted on. As the no. of people using the crypto increases the donations using the crypto will also increase.

Another aspect of `BlockFund` is transparency, since it's built on top of blockchain it's fully transparent and there is no central authority whi is controling this platform, there will be no fraud where the singer person can withdraw or scam the site.

**Since everyone is anonymous, what if a scammer tries to raise fund ?**
We can solve this problem by first validating the person/Organization who wants to raise funds.
I didn't have time to implement it, but it'll be done in the future development.


## 🦾 Challenges Faced
First of all, I want to thank `Hack the mountains` team to organize this beautiful hackathon and to give me the oppurtunity to learn and build my DAPP.
Before this hackathon i din't knew much about Blockchain and DAPP dev. But after joining it i spend a lot of time to research and figure out how to build DAPP.
### 🔍 Project Searching Face
Initially i faced trouble setting up all the development tools needed specially for writting smart contract and deploying it. I was new to TEzos world and Blockchain in general but then i joined the Official Telegram group of SmartPy. The admin who is probably the creator of SmartPy was so helping he helped me to set up and solve even tiny bugs, i really want to thank him.

### 👨🏾‍💻 During the Development
When i started working ont my Idea, using Blockchain and when i started writing the client / Web App more problems started to emerge. Initially i wasn't able to connec to my wallent then sign the transaction, then send the tezos from my wallet to the contract. I was feeling that i will not be able to complete it but the Official Telegram group of `SmartPy` and `Taquito` helped me a lot they helped me solve my silly mistakes.

### 🌐 During Deployment.
Initially i was thinking to use `Azure` but then Linode was a MLH sponser and this hackathon was a MLH sponsered so i got free credits on linode, and honestly after trying it i found that it's cheaper than `Azure`. I face some issues during the configuration of Domain Name and setting up A name record and setting up nginx server. but i was able to fix it after doing some research.


## 🔥 Future Development
- [ ] Improve the UI tremendously.
- [ ] Improve the Smart Contract.
- [ ] Code Refactoring. 


## ☎️ Let's Connect 
- **Twitter:** https://twitter.com/vivekascoder
- **Discord:** https://discord.gg/8dC7QAF6r8
- **Personal Blog:** https://blog.divcorn.com

💰️ Support the project development 
Ξ Ethereum: 0xAF5D27A3095C545CfB4357E5e1061ADe2Ea8911C
ꜩ Tezos: tz1UxnruUqq2demYbAHsHkZ2VV95PV8MXVGq
