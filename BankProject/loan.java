package BankProject;
import java.util.*;

public class loan extends BankCard {
    private int loanamount;
    private String status;
    private String job;
    private HashMap <String,Integer> loans;
    private int rent;
    private int salary;
    public enum validation{
        CHECKING,
        UNSUCCESSFUL,
        SUCCESSFUL
        
    };
    




    loan(String j,int r,int s){
        super();
        this.job = j;
        this.rent = r;
        this.salary = s;
    }


    public void ApplyForLoan(int l){
        validation LoanCheck = validation.CHECKING;
        if(creditScore < 500){
            LoanCheck = validation.UNSUCCESSFUL;
        }
        else{
            if(salary >= l*2 && rent <= salary/10){
                loans.put(name,l);
                LoanCheck = validation.SUCCESSFUL;
            }
            else{
                LoanCheck = validation.UNSUCCESSFUL;
            }
        }
        System.out.println("The loan is " + LoanCheck);
    }

    public void CheckStatus(){


    }

    

}
