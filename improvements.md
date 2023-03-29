- accept two arguments as one word like "publicity stunt"
- make a django app that has an input field you enter the word and the text appears in a div in the page for you, may be get a couple of photos too from google, and a button to get new photos if current photos are not of quality or descriping the word clearly 
- output you entered the word wrong if an output like this occured
 def delerious
------------------------------
  تهذي هذيان يهذي أهذي هاذي
  يهلوس وهذياني منفعلا مصاب بالهذيان مهتاج
  يهذون تهلوس معهاكانت متوهمه
------------------------------
Traceback (most recent call last):
  File "/media/itsmohamedyahia/HORIZON/playPath/python/scraping-dictionary/def.py", line 101, in <module>
    main()
  File "/media/itsmohamedyahia/HORIZON/playPath/python/scraping-dictionary/def.py", line 95, in main
    print_definitions(def1_divs)
  File "/media/itsmohamedyahia/HORIZON/playPath/python/scraping-dictionary/def.py", line 62, in print_definitions
    def_wrapped_list = textwrap.wrap(def_divs[0].text, width=80)
IndexError: list index out of range


