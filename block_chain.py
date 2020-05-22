from time import time as td
from hashlib import sha256
from json import dumps




class Block:

    def __init__(self,index,transaction,timestamp,prehash):

        self.index=index
        self.transaction=transaction
        self.timestamp=timestamp
        self.prehash=prehash
        self.nonce=0
        
       
    def gen_hash(self):
        
        return sha256(dumps(self.__dict__).encode()).hexdigest()


    
class Blockchain:

    difficulty =2
    uc_trans=[]

    def __init__(self):

        
        self.chain=[]
        self.genesis_block()

    def genesis_block(self):

        
        genesis=Block(0,[], td(), 0)
        genesis.hash_h=genesis.gen_hash()
        self.chain.append(genesis)

    def proof_of_work(self,block):

        
        block.nonce=0
        k=block.gen_hash()
        
        

        while not (k.startswith('0'*self.difficulty)): 
               block.nonce+=1
               k=block.gen_hash()
               

        
        return k

    def valid_proof(self,block,block_hash):

        
        result= (block_hash.startswith('0'*self.difficulty)) and (block_hash==block.gen_hash())
        
        return result

    def unconfirmed_transaction(self,transaction):
        
        self.uc_trans.append(transaction)

    def add(self,block,proof):

        
        if not (block.prehash==self.chain[-1].hash_h):
               return False
        if not (self.valid_proof(block,proof)):
               return False

        
        block.hash_h= proof
        self.chain.append(block)
        return True

    def mine(self):
        
        
        if not self.uc_trans:
                return False

        k=self.chain[-1]        
        new_block=Block(k.index+1,self.uc_trans,td(),k.hash_h)

        proof=self.proof_of_work(new_block)
        #for verifying
        print('\n'+proof)

        self.add(new_block,proof)
        self.uc_trans=[]

    def chain_len(self):

        return len(self.chain)
                
Test=Blockchain()
c=0
while(1):
    trans=input('Enter transaction details')
    Test.unconfirmed_transaction(trans)
    Test.mine()
    k=input('\n(C)ontinue/(Any key) Exit')
    if k not in ('C','c'):
        break
print(Test.chain_len())

    
    
    
    

        

               
               

                       


 
               

        


