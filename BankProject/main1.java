package BankProject;

public class main1 {
    public static void main(String[] args) {
        BankCard Natwest = new BankCard("Nebil", "0774512412","18 George Yard", "NN@gmail.com");
        System.out.println(Natwest.getPin());
        //Natwest.ChangeDetails("N3B1L@gmail.com");
        System.out.println(Natwest.email);
        Natwest.setBalance(1000);
        //Natwest.Spend(900);
        Natwest.Deposit_Withdraw(500);
        System.out.println(Natwest.getBalance());


    }
}
