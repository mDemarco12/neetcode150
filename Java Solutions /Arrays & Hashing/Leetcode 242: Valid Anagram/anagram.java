import java.util.Arrays;

public class anagram {
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
     // This solution uses a HashTable 
    public boolean isAnagramOptimal(String s, String t){
        // Edge case: if lengths do not match, they aren't anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Create an int array of 26 chars a..z
        int[] count = new int[26]; 
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++; // subtract the char s at index i, then increment
            count[t.charAt(i) - 'a']--; // ditto, but decrement. 
        }

        // for val in count
        for(int val : count) {
            // if value does not equal 0, they are not anagrams; false
            if(val != 0) {
                return false;
            }
        }
        // if they are equal to 0, return true. 
        return true; 

    }

}
