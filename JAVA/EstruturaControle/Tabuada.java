import java.util.Scanner;

public class Tabuada {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe um numero");
        int n =   scanner.nextInt();

        int cont= 0;

        while (cont <= 10){
        
       int  operacao = n * cont ;

        System.out.printf(" tabuada de %d x %d=%d\n", n ,cont, operacao);
        cont++;

        }
            
        
    }

}