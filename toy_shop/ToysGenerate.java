package intermediate_control_work.toy_shop;

import java.util.ArrayList;
import java.util.Random;

public class ToysGenerate {
    private static ArrayList<Toy> listToys = new ArrayList<>(); // Список игрушек
    
    public ToysGenerate(int size) {
        Random variable = new Random();

        for (int i = 0; i < size; i++) {
            Toy j = new Toy();
            j.setId(i);
            j.setName(String.format("Игрушка-%d", i));
            j.setAmount(variable.nextInt(1,4));
            j.setDrop(variable.nextDouble());
            listToys.add(j);
        }
    }

    public ArrayList<Toy> getList() { return listToys;}
}
