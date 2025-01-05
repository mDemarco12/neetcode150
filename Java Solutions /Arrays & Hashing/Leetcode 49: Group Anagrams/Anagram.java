import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Anagram {
    public List<List<String>> groupAnagramsSorting(String[] strs)
    {
        /* Time Complexity: O(m*nlogn): Mem: O(m*n)*/
        /* Sorting is dependant on ## of Strings (m) and length of strings (n)*/
        Map<String, List<String>> result = new HashMap<>();
        for (String s: strs)
        {
            //Create a new character array
            char[] charArray = s.toCharArray();
            // sort the characters
            Arrays.sort(charArray);
            // Store the sorts into sortedS
            String sortedS = new String(charArray);
            // Add key value pair if it DNE 
            result.putIfAbsent(sortedS, new ArrayList<>());
            // Get sortedS and add it to result
            result.get(sortedS).add(s); 

        }
        return new ArrayList<>(result.values()); 
    }
    /* Time Complexity: O(m*n): Mem: O(m) */
    /* HashTable is concerned with m and n, but memory only requieres m since the table and length of string are not connected. */
    public List<List<String>> groupAnagramsHashTable(String[] strs)
    {
        Map<String, List<String>> res = new HashMap<>(); 

        for(String s: strs)
        {
            int[] count = new int[26]; 
            for (char c: s.toCharArray()) 
            {
                count[c - 'a']++; 
            }
            
            
            String key = Arrays.toString(count); 
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values()); 

    }

    public static void output()
    {
        Anagram sol = new Anagram(); 

        String[] list1 = {"act","pots","tops","cat","stop","hat"};
        String[] list2 = {"x"};

        // Set 1: 
        System.out.println("List 1: ");
        System.out.printf("Here are the anagrams for the following group: %s\n", Arrays.toString(list1));
        System.out.println("Here are the sorted groups: ");
        System.out.println(sol.groupAnagramsSorting(list1));
        System.out.println();

        // Set 2: 
        System.out.println("List 2: ");
        System.out.printf("Here are the anagrams for the following group: %s\n", Arrays.toString(list2));
        System.out.println("Here are the sorted groups: ");
        System.out.println(sol.groupAnagramsSorting(list2));
        System.out.println();
    
        // Set 1 HashMap: 
        System.out.println("List 1 (HashMap): ");
        System.out.printf("Here are the anagrams for the following group: %s\n", Arrays.toString(list1));
        System.out.println("Here are the sorted groups: ");
        System.out.println(sol.groupAnagramsHashTable(list1));
        System.out.println();

        // Set 2: 
        System.out.println("List 2 (HashMap): ");
        System.out.printf("Here are the anagrams for the following group: %s\n", Arrays.toString(list2));
        System.out.println("Here are the sorted groups: ");
        System.out.println(sol.groupAnagramsHashTable(list2));

    }

}
