# Working with JSON Objects

## ACS 1710 - Module 3: Lesson 3

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Write JSON objects (i.e. Python dictionaries) containing nested data.
- Retrieve values from nested JSON objects using Python dictionary syntax.

# Video Companions 🎥

[Vid 1 - Creating `JSON` objects in Python](https://youtu.be/t1t6crpMRgo)

Vid 1 - Creating `JSON` objects in Python

[Vid 2 - Returning `JSON` objects in a Flask route](https://youtu.be/HztSwyxdQzo)

Vid 2 - Returning `JSON` objects in a Flask route

# Exercises 💪

Complete the exercise in [this repl.it](https://repl.it/team/WebArchitecture/Module-302DictionariesPractice) and submit your work.

# Written Companion 🗒

<aside>
🤔 How do we efficently package information so that tens of thousands of users can be served as quickly as possible?

</aside>

---

`JSON` stands for **JavaScript Object Notation**. 

<aside>
🚨 A `JSON` object can be used by languages other than Javascript! `JSON` objects find their origins in Javascript and therefore look similar to them—but `JSON` objects also look quite similar to Python objects too.

</aside>

<aside>
💡 Many programming languages can interpret `JSON` objects because they are nothing more then an **object notation**—which means that the object always uses the same predictable **key-value** pairs.

</aside>

```json
{
	"type": "success",
	"value": {
		"id": 493,
		"joke": "Chuck Norris can binary search unsorted data.",
		"categories": ["nerdy"]
	}
}
```

Fig *1 - a `JSON` object with several **key-value** pairs.*

- *Note: A `JSON` object looks identical to Python's `dictionary` data structure because both use the same **key-value** pair format*

<aside>
🚨 Notice that the `JSON` object in *Fig 1* does not have any variable declarations! `JSON` objects exist to be packaged and/or sent across the internet. As a result, a `JSON` file only contains object data **to be assigned by the requesting function.**

</aside>

Since `JSON` objects always use the same notation pattern and can be transported efficently, they have become a standard API format to utilize for passing data across networks.

```python
# a JSON object translated into Python
my_info = {
   'name': 'Fluffy',
   'likes': ['tennis balls', 'walks'],
   'address': {
       'street': '555 Post St',
       'city': 'San Francisco'
   }
}

# accessing the `my_info` object's `address` property, then the `street` property
street_address = my_info['address']['street']
```

*Fig 2 - a `JSON` object implemented into a Python file*

- *Consider how a `JSON` object can be assigned to a Python variable—would it be possible to import the `my_info` data from a `JSON` object instead of hard coding it here?*
- *Note: Notice how each of the object's properties must be accessed to go deeper into the child objects*