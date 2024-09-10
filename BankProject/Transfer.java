package BankProject;

public class Transfer extends BankCard{
    int sendingAmount;
    BankCard namesender;
    int sortCode;

    Transfer(String Name,String Email,int Amount){
        super();
        this.name = Name;
        this.email = Email;
        this.sendingAmount = Amount;
    }

    public void LocalTransfer(BankCard sender,int sortcode,int sending_amount){
        if(sending_amount > balance){
            System.out.println("Not enough to send money");
        }
        else{
            if(sender.name == name && sender.email == email){
                balance = balance - sending_amount;
                sender.balance = balance + sending_amount;
            }
        }
        
    }




    






    
}
