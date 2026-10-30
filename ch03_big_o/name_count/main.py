def count_names(list_of_lists, target_name):
    """
    Core task: Traverse a nested list structure to count all occurrences of a specific `target_name`

        Count how many times `target_name` appears across all names in a nested list of lists.

        Args:
            `list_of_lists`: A list containing inner lists of strings (names)
            `target_name`: The name to count (str)

        Returns:
            int: The total count of `target_name` across all inner lists

        Time Complexity: O(n) where n is the total number of names
                         (or O(m * n) with m outer lists and n average inner length)

                         n = number of lists
                         m = average length of each list

        Space Complexity: O(1) - no extra space beyond a counter
        """
    # Step 1. Initialize a counter for the target name
    count = 0

    # Step 2. Iterate over each inner list
    for inner_list in list_of_lists:

        # Step 3. Iterate over each name in the inner list
        for name in inner_list:

            # Step 4. If the current name matches the target, increment the counter
            if name == target_name:
                count += 1

    return count



