package BankProject;
import java.util.*;
import java.io.*;


public class BankCard{
    protected String name;
    protected String number;
    protected String address;
    protected String email;
    private int pin;
    public Scanner input;
    public int detailChange;
    protected int balance;
    protected int creditScore;


    BankCard(String name,String number,String address,String email){
        this.name = name;
        this.number = number;
        this.address = address;
        this.email = email;
        this.pin = 0000;
    }

    BankCard(){

    }

    public void setPin(int p){
        pin = p;
    }

    public int getPin(){
        return pin;
    }

    public void setBalance(int b){
        balance = b;
    }

    public int getBalance(){
        return balance;
    }

    public int getcreditScore(){
        return creditScore;
    }

    public void setcreditScore(int cs){
        creditScore = cs;
    }

    protected void AccountHistory(){
        try{
            FileWriter Account_History = new FileWriter("C:/Users/nebil/OneDrive/Documents/NN/Nebil 16+/Computer Science University/CV/Portfolio/BankProject/History.txt");
            Account_History.write(String.valueOf(balance));
            Account_History.close();
        } catch(IOException e){
            e.printStackTrace();
        }
    }



    public void ChangeDetails(String accountDetail){ //In here they add the account detail they want to change
        input = new Scanner(System.in);
        System.out.println("Please confirm what account detail you need to change");
        System.out.println("Type 1 for Name, Type 2 for Number, Type 3 for Address, Type 4 for Email");
        detailChange = input.nextInt();
        switch(detailChange){
            case 1:
                if(accountDetail.length() > 2)
                    name = accountDetail;
                else
                    System.out.println("Error");
                break;
            case 2:
                if(accountDetail.length() == 12)
                    number = accountDetail;
                else
                    System.out.println("Error");
                break;
            case 3:
                if(accountDetail.length() > 2 && accountDetail.contains(" "))
                    address = accountDetail;
                else
                    System.out.println("Error");
                break;
            case 4:
                if(accountDetail.length() > 2 && accountDetail.contains("@"))
                    email = accountDetail;
                else
                    System.out.println("Error");
                break;
            }
    }

    public void Spend(int amount){
        Scanner pinput = new Scanner(System.in);
        System.out.print("Enter Pin: ");
        int pin_input = pinput.nextInt();
        if(pin_input == pin){
            if(balance >= amount){
                setBalance(balance-amount);
                AccountHistory();
                System.out.println("Card Verified");
            }
            else{
                System.out.println("Balance too low");
            }
        }
        else{
            System.out.println("Incorrect Pin");
        }        
    }


    public void Deposit_Withdraw(int amount){
        Scanner pinput = new Scanner(System.in);
        System.out.print("Enter Pin: ");
        int pin_input = pinput.nextInt();
        System.out.println("Enter 1 for Withdraw, Enter 2 for deposit");
        int options = pinput.nextInt();
        if(pin_input == pin){
            if(options == 1){
                if(balance >= amount){
                    setBalance(balance-amount);
                    AccountHistory();
                    System.out.println("Card Verified");
                }
                else{
                    System.out.println("Balance too low");
                }
            }
            else if(options == 2){
                setBalance(balance+amount);
                AccountHistory();
            }
            else{
                System.out.println("Unknown Option");
            }
        }
        else{
            System.out.println("Incorrect Pin");
        }  
    }

    

    










}