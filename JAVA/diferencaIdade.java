import java.util.Scanner;

public class diferencaIdade{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o nome da Pessoa 1");
        String P1 = scanner.nextLine();
        System.out.println("Informe o idade da Pessoa 1");
        int idade1 = scanner.nextInt();
        System.out.println("Informe o nome da Pessoa 2");
        String P2 = scanner.nextLine();
        System.out.println("Informe o idade da Pessoa 2");
        int idade2 = scanner.nextInt();


        int diferenca = idade1 - idade2 ;

        System.out.printf("A diferença %d",diferenca);

    }


}