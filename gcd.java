
public class gcd {
    static int recurCount = 0;

    public static void main(String[] args) {
        int[][] pairs = getNumPairs();
    
        int[] maxConResults = consecutiveGcd(pairs[0][0], pairs[0][1]);
        int[] maxEucResults = getEuclidResult(pairs[0][0], pairs[0][1]);

        int[] minConResults = consecutiveGcd(pairs[0][0], pairs[0][1]);
        int[] minEucResults = getEuclidResult(pairs[0][0], pairs[0][1]);

        int totalCon = maxConResults[1];
        int totalEuclid = maxEucResults[1];

        for (int i=1; i < pairs.length; i++){
            int[] currConResults = consecutiveGcd(pairs[i][0], pairs[i][1]);
            int[] currEucResults = getEuclidResult(pairs[i][0], pairs[i][1]);

            int conCount = currConResults[1];
            int eucCount = currEucResults[1];

            totalCon += conCount;
            totalEuclid += eucCount;

            if (conCount < minConResults[1])
                minConResults = currConResults;

            if (conCount > maxConResults[1])
                maxConResults = currConResults;

            if (eucCount < minEucResults[1])
                minEucResults = currEucResults;

            if (eucCount > maxEucResults[1])
                maxEucResults = currEucResults;
        }

        int conAvg = totalCon / pairs.length;
        int eucAvg = totalEuclid / pairs.length;

        String conMostOutput = String.format("The most number of iterations used is (%d) for GCD(%d, %d) = %d.", 
                                            maxConResults[1], maxConResults[2], maxConResults[3], maxConResults[0]);

        String conLeastOutput = String.format("The least number of iterations used is (%d) for GCD(%d, %d) = %d.", 
                                            minConResults[1], minConResults[2], minConResults[3], minConResults[0]);

        String conAvgOutput = String.format("The average number of iterations used for all 100 pairs is (%d).", conAvg);

        String eucMostOutput = String.format("The most number of iterations used is (%d) for GCD(%d, %d) = %d.", 
                                            maxEucResults[1], maxEucResults[2], maxEucResults[3], maxEucResults[0]);

        String eucLeastOutput = String.format("The least number of iterations used is (%d) for GCD(%d, %d) = %d.", 
                                            minEucResults[1], minEucResults[2], minEucResults[3], minEucResults[0]);

        String eucAvgOutput = String.format("The average number of iterations used for all 100 pairs is (%d).", eucAvg);

        System.out.println("Consectutive Algorithm:");
        System.out.println(conMostOutput);
        System.out.println(conLeastOutput);
        System.out.println(conAvgOutput);

        System.out.println();

        System.out.println("Euclidean Algorithm:");
        System.out.println(eucMostOutput);
        System.out.println(eucLeastOutput);
        System.out.println(eucAvgOutput);

    }

    public static int randInt(int min, int max){ 
        int random_int = (int)Math.floor(Math.random()*(max-min+1)+min);
        return random_int;
    }

    public static int[][] getNumPairs (){
        int[][] arr = new int[100][2];

        for (int i=0; i < arr.length; i++){
            arr[i][0] = randInt(3000,300000);
            arr[i][1] = randInt(3000,300000);
        }

        return arr;
    }

    public static int[] consecutiveGcd(int a, int b){
        int[] ans = new int[4];
        int minValue = Math.min(a, b);
        int copyMin = minValue;

        for (int i=1; i <= copyMin; i++){
            if (a % minValue == 0)
                if (b % minValue == 0){
                    ans[0] = minValue;
                    ans[1] = i;
                    break;
                }
                else
                    minValue--;
            else
                minValue--;
        }
        ans[2] = a;
        ans[3] = b;

        return ans;
    }

    public static int[] getEuclidResult(int a, int b){
        int[] ans = new int[4];

        ans[0] = euclidGcd(a, b);
        ans[1] = recurCount;
        ans[2] = a;
        ans[3] = b;
        recurCount = 0;

        return ans;
    }

    public static int euclidGcd(int a, int b){
        if (b == 0)
            return a;
        else{
            recurCount++;
            return euclidGcd(b, a%b);
        }
    }
}