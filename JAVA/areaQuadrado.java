import java.util.Scanner;

public class areaQuadrado {


    public static void main(String[] args) {
        
        //inicia o scanner para lê a entrada do scanner
        Scanner scanner = new Scanner(System.in);

        //recebe o lado A
        System.out.println("Informe o Lado A do Quadrado");
        int A= scanner.nextInt();
        //recebe o lado B 
        System.out.println("Informe o lado B do Quadrado");
        int B = scanner.nextInt();

        int area=A*B;

        System.out.printf("A area do quadrado é:%d20",area);
    } 
}