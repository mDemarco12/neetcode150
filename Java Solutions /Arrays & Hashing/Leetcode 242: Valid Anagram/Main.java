public class main {
    public static void main(String[] args) {

        anagram solution = new anagram(); // Object

        // Declare our sample Strings
        String s1 = "racecar";
        String s2 = "hello";
        String t1 = "carrace";
        String t2 = "hellop";

        // Sorting Solution
        long startTime1 = System.nanoTime();
        boolean sol1 = solution.isAnagramSorting(s1, t1);
        boolean sol2 = solution.isAnagramSorting(s2, t2);
        long endTime1 = System.nanoTime();
        long duration1 = (endTime1 - startTime1);

        // Optimal
        long startTime2 = System.nanoTime();
        boolean sol3 = solution.isAnagramOptimal(s1, t1);
        boolean sol4 = solution.isAnagramOptimal(s2, t2);
        long endTime2 = System.nanoTime();
        long duration2 = (endTime2 - startTime2);

        System.out.printf("Sorting Solution Results for Sorting:\nS1: '%s' and T1: '%s' are %s\n", s1, t1, sol1);
        System.out.printf("S2: '%s' and T2: '%s' are %s\n", s2, t2, sol2);
        System.out.printf("Time taken: %d nanoseconds\n\n", duration1);

        System.out.printf("Sorting Solution Results for Optimal:\nS1: '%s' and T1: '%s' are %s\n", s1, t1, sol3);
        System.out.printf("S2: '%s' and T2: '%s' are %s\n", s2, t2, sol4);
        System.out.printf("Time taken: %d nanoseconds\n\n", duration2);

        // solutionOutput();
    }
}
