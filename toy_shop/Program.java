package intermediate_control_work.toy_shop;

public class Program {
    //ArrayList<String> candidate; // Список кандидатов на выигрыш

    public static void main(String[] args) {
        ToysGenerate a = new ToysGenerate(10);

        for (Toy b : a) {
            System.out.println(b.getId());
            System.out.println(b.getName());
            System.out.println(b.getAmount());
            System.out.println(b.getDrop());
        }
    }
}
