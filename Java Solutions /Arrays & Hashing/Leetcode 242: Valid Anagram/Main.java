import java.util.Arrays;

public class Main {


    public boolean isAnagramSorting(String s, String t){
        // Edge case: If the lengths are !=, False
        if (s.length() != t.length()){
            return false; 
        }

        // Create character arrays for each
        char[] sSort = s.toCharArray();
        char[] tSort = t.toCharArray();

        // Sort
        Arrays.sort(sSort);
        Arrays.sort(tSort); 
        
        // Return the value 
        return Arrays.equals(sSort, tSort); 
    }

    public static void main(String[] args) {
        // Declare our sample Strings
        Main solution = new Main();
        
        String s1 = "racecar"; 
        String s2 = "hello"; 
        String t1 = "carrace"; 
        String t2 = "hellop"; 

        

        boolean sol1 = solution.isAnagramSorting(s1, t1);
        boolean sol2 = solution.isAnagramSorting(s2, t2); 

        System.out.printf("S1: '%s' and T1: '%s' are %s\n", s1, t1, sol1);
        System.out.printf("S2: '%s' and T2: '%s' are %s\n", s2, t2, sol2);
    }
    
}
