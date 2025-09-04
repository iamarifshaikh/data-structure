package OOPs;

abstract class GameCharacter{
    String name;

    GameCharacter(String name) {
        this.name = name;
    }

    void move(){
        System.out.println(name + "is moving!");
    }

    abstract void attack();
    
}

class Weapon{
    String name;
    int damage;

    Weapon(String name, int damage) {
        this.name = name;
        this.damage = damage;
    }

    void use(){
        System.out.println("Using " + name + " with damage of "+ damage);
    }
}

class Knight extends GameCharacter{
    Weapon weapon;

    Knight(String name, Weapon weapon) {
        super(name);
        this.weapon = weapon;
    }

    @Override
    public void attack(){
        weapon.use();
        System.out.println("Swinging sword to attack!");
    } 
    
}

class Archer extends GameCharacter{
    Weapon weapon;

    Archer(String name,Weapon weapon) {
        super(name);
        this.weapon = weapon;
    }

    @Override
    public void attack(){
        weapon.use();
        System.out.println("Readying bow and arrow to attack!");
    } 
    
}

public class Main {
    public static void main(String[] args) {
        Weapon sword = new Weapon("Excalibur", 50);
        Weapon bow = new Weapon("Longbow", 30);
        
        Knight knight = new Knight("Arthur",sword);
        Archer archer = new Archer("Robin",bow);

        knight.move();
        knight.attack();

        System.out.println("--------------------------------------------------------");

        archer.move();
        archer.attack();
    };
};