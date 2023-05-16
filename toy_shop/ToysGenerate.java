package intermediate_control_work.toy_shop;

import java.util.Random;

public class ToysGenerate {
    ArrayList<Toy> listToys; // Список игрушек
    
    public ToysGenerate(int size) {
        Random variable = new Random();

        for (int i = 0; i < size; i++) {
            Toy j = new Toy();
            j.setId(i);
            j.setName(String.format('Игрушка-%d', i));
            j.setAmount(variable.nextInt(1,4));
            j.setDrop(variable.nextDouble());
        }
    }
}
