
// WORKFLOW

import io;
import string;


@dispatch=WORKER
(string output) python_persist(string code, string expr="\"\"") "turbine" "0.1.0"
[ "set <<output>> [ turbine::python 1 <<code>> <<expr>> ]" ];


(string tasks) get_tasks()
{
    tasks = python_persist("import swift_e",
                           "swift_e.get_tasks()");
}

//(string result) task(string arguments)
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

(boolean result) run_tasks(string taskstring)
{
    return_val = task(taskstring) =>
        put_results(return_val) =>
        result = true;
}

loop()
{
    for (boolean b = true; b; b=c){

        printf("In loop");
        boolean c;
        tasks = get_tasks();
        printf("Running task : %s", tasks);
        c = run_tasks(tasks);
        /*
        if (tasks == "DONE") {
            printf("Done");
            c = false;

        }else{
        }
        */
    }
}

loop();
