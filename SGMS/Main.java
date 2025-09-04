package SGMS;

import java.util.*;

class ReportCard {
    HashMap<String, Integer> subjects;

    ReportCard() {
        this.subjects = new HashMap<>();
    }

    void addSubject(String subject, int marks) {
        if (subjects.containsKey(subject))
            System.err.println("Subject already in report card!");
        else
            subjects.put(subject, marks);
    }

    void updateMarks(String subject, int marks) {
        if (!subjects.containsKey(subject))
            System.err.println("No subject called " + subject + " in report card");
        else
            subjects.put(subject, marks);
    }

    double calculateAverage() {
        if (subjects.isEmpty()) return 0;
        int total = 0;
        for (int marks : subjects.values()) {
            total += marks;
        }
        return (double) total / subjects.size();
    }

    void displayReport() {
        for (Map.Entry<String, Integer> entry : subjects.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
        System.out.printf("Average Marks: %.2f%n", calculateAverage());
        System.out.println("----------------------");
    }
}

class Student {
    String name;
    int rollNumber;
    ReportCard reportCard;

    Student(String name, int rollNumber) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.reportCard = new ReportCard();
    }

    void displayDetails() {
        System.out.println("Name: " + name + ", Roll Number: " + rollNumber);
        reportCard.displayReport();
    }
}

public class Main {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();

        Student s1 = new Student("Arif", 59);
        s1.reportCard.addSubject("Math", 95);
        s1.reportCard.addSubject("Science", 88);

        Student s2 = new Student("Shubham", 42);
        s2.reportCard.addSubject("Math", 85);
        s2.reportCard.addSubject("English", 91);

        students.add(s1);
        students.add(s2);

        for (Student s : students) {
            s.displayDetails();
        }
    }
}
