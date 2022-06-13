from xml.etree.ElementInclude import include


def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    # for num in nums:
    #     print(include(range(lowest, highest)))

    # for num in nums:
    #   if num >= lowest and num <= highest :
    #     print(num)

    r = range(lowest, highest+1)
    for num in nums:
      if num in r:
        print(num)
        

          


in_range([10, 20, 30, 40, 50], 15, 30)            
