
// WORKFLOW

import python;
import string;

(string tasks) get_tasks()
{
  tasks = python_persist("import swift_e",
                         "swift_e.get_tasks()");
}

(string result) task(string arguments)
{
  result = python_persist("import swift_e",
                          "repr(swift_e.task(\"%s\"))" % arguments);
}

(boolean result) put_results(string results)
{
  python_persist("import swift_e",
                 "swift_e.put_results(\"%s\")" % results) =>
    result = true;
}

(boolean result) run_tasks(string tasks)
{
  string task_strings[] = split(tasks, ";");
  string results[];
  foreach task_string,i in task_strings
  {
    results[i] = task(task_string);
  }
  result = put_results(join(results, ";"));
}

loop()
{
  for (boolean b = true; b; b=c)
  {
    boolean c;
    tasks = get_tasks();
    if (tasks == "DONE")
    {
      c = false;
    }
    else
    {
      c = run_tasks(tasks);
    }
  }
}

loop();
