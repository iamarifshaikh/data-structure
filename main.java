public class main{
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("ABCDCBA");
        
        if(isPlaindrome(sb)){
            System.out.println("Hooray! The Given String Is Plaindrome");
        }else{
            System.out.println("It is not a palindrome");
        }
    }
    
    public static boolean isPlaindrome(StringBuilder sb){
        int i = 0;
        int j = sb.length() - 1;

        while (i <= j){
            if (sb.charAt(i) != sb.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;   
    };
}