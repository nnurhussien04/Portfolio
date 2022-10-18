import java.sql.SQLOutput;

public class Tutorial {

    static int increment(int number){
        number++;
        return number;
    }

    public static void check(String name){
        if (name.isEmpty()){
            System.out.println("error");
        }
        else{
            System.out.println("success");
        }
    }



    public static void main(String[] args){
        System.out.println("Hello");
        int number;
        number = 5;
        int number2 = 9;
        byte b = 120;
        short snumber = 1000;
        long lnumber = 234L;
        float fnumber = 94.5f;
        double dnumber = 3.67;
        System.out.println(number + " " + number2 + " " + snumber + " " + lnumber + " " + dnumber + " " + fnumber);
        number++;
        System.out.println(number);
        number--;
        System.out.println(number);
        System.out.println(number+number2);
        System.out.println(number-number2);
        System.out.println(number*number2);
        System.out.println(number/number2);
        System.out.println(number%number2);
        boolean true1 = true;
        boolean false1 = false;
        System.out.println(true1 + " " + false1);
        System.out.println(5 > 9 ? 5:9);
        number = (int) dnumber;
        System.out.println(number);
        int [] array = {9,5,2,4,1};
        int [] array2 = new int[8];
        int n = 0;
        for(int a:array2) {
            array2[a] = n +  2;
            System.out.println(array2[a]);
            n++;
        }
        System.out.println(array.length);
        int ifvar = 24;
        int elsevar = 12;
        if (ifvar == 24){
            System.out.println(ifvar);
        }
        else{
            System.out.println(elsevar);
        }
        elsevar = 25;
        switch (elsevar){
            case 10:
                System.out.println(10);
                break;
            case 15:
                System.out.println(15);
                break;
            case 20:
                System.out.println(20);
                break;
            default:
                System.out.println("Unrecognised");
                break;
        }
        for(int j=0;j<9;j++){
            System.out.println("Repeat");
        }
        int [] array3 = {2,4,6,8,10};
        for(int even:array3){
            System.out.println(even);
        }
        int whileint = 0;
        while (whileint <= 20){
            System.out.println(whileint);
            whileint += 2;
        }
        boolean worked = false;
        /*do{
            System.out.println(whileint);
            whileint=-2;
            worked = true;
        }while (whileint > 0);*/
        System.out.println(whileint);
        int x = 100;
        while(x>0){
            x--;
            if(x==90){
                System.out.println(x);
                continue;
            }
            if(x==50){
                System.out.println(x);
                break;
            }
        }

        System.out.println(increment(5));
        check("");




    }

}
