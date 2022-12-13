# INSERT THE WORKSHOP HERE



EPIC
e1 = db.session.query(Epic).filter_by(id=1)

def serialize():
  stories = self.stories
  all_tasks = []
  for s in self.stories:
   all_tasks.extend(s.tasks)
  all.tasks.sort(key=lambda x: x['updated_on'])
  
  issues = []
  sp, tp = 0, 0
  while sp < len(stories) or tp < len(all_tasks):
    if stories[sp]['updated_on'] <= all_tasks[tp]['updated_on']:
      issues.append(stories[sp])
      sp += 1
    else:
      issues.append(tasks[tp])
      tp += 1

  return {

  }

a1 = [1,2,3]
a2 = [4,5,6]

a1.extend(a2) # [1,2,3,4,5,6]

STORIES

TASKS