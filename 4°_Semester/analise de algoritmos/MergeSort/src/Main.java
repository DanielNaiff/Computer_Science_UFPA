public class Main {
    public static void main(String[] args) {
        int[] array = {8, 2, 5, 3, 4, 7, 6, 1};
        mergeSort(array);
        for(int i: array){
            System.out.print(i + " ");
        }
    }

    private static void mergeSort(int[] array) {
        int length = array.length;
        if (length <= 1) return;

        int middle = length / 2;
        int[] leftArray = new int[middle];
        int[] rightArray = new int[length - middle];

        // Fill the leftArray with the first half of array
        for (int i = 0; i < middle; i++) {
            leftArray[i] = array[i];
        }

        // Fill the rightArray with the second half of array
        for (int i = middle; i < length; i++) {
            rightArray[i - middle] = array[i];
        }

        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(leftArray, rightArray, array);
    }


    private static void merge(int[] leftArray, int[] rightArray, int[] array) {
        int leftSize = leftArray.length;
        int rightSize = rightArray.length;
        int i = 0, l = 0, r = 0;

        // Merging process
        while (l < leftSize && r < rightSize) {
            if (leftArray[l] < rightArray[r]) {
                array[i] = leftArray[l];
                i++;
                l++;
            } else {
                array[i] = rightArray[r];
                i++;
                r++;
            }
        }

        // Copy remaining elements from leftArray (if any)
        while (l < leftSize) {
            array[i] = leftArray[l];
            i++;
            l++;
        }

        // Copy remaining elements from rightArray (if any)
        while (r < rightSize) {
            array[i] = rightArray[r];
            i++;
            r++;
        }
    }

}
