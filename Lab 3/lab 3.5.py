record_collection = {
    2548: {
        'albumTitle': 'Slippery When Wet',
        'artist': 'Bon Jovi',
        'tracks': ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
        'albumTitle': '1999',
        'artist': 'Prince',
        'tracks': ['1999', 'Little Red Corvette']
    },
    1245: {
        'artist': 'Robert Palmer',
        'tracks': []
    },
    5439: {
        'albumTitle': 'ABBA Gold'
    }
}

def update_records(dictionary_record, record_id, prop, value):
  if prop != 'tracks':
      if value != '':
          if record_id not in dictionary_record:
              dictionary_record[record_id] = {}
          dictionary_record[record_id][prop] = value
      elif record_id in dictionary_record and prop in dictionary_record[record_id]: del dictionary_record[record_id][prop]
  else:
      if value == '':
          if record_id in dictionary_record and prop in dictionary_record[record_id]: del dictionary_record[record_id][prop]
      elif record_id in dictionary_record:
          if prop not in dictionary_record[record_id]: dictionary_record[record_id][prop] = []
          if value: dictionary_record[record_id][prop].append(value)
      else:
          if value: dictionary_record[record_id] = {prop: [value]}
  return dictionary_record

update_function = input("Input: ").split()
print(update_records(record_collection, int(update_function[0]), update_function[1], update_function[2]))