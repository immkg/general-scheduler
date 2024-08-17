from util.range_constraints import *
from util.utils import *
from controller.Implications.ComfortImplications import *
from controller.Implications.StandardImplications import *
from controller.Parser import *
from util.utils import *
from controller.StaticVariables import *


def simple_interface(input_dict):

    StaticVariables.duration = input_dict['duration']

    for (t, s, g, n) in list(StaticVariables.duration.keys()):
        StaticVariables.num_t = max([StaticVariables.num_t, t + 1])
        StaticVariables.num_s = max([StaticVariables.num_s, s + 1])
        StaticVariables.num_g = max([StaticVariables.num_g, g + 1])

    StaticVariables.teachers = np.array(list(range(StaticVariables.num_t)))
    StaticVariables.subjects = np.array(list(range(StaticVariables.num_s)))
    StaticVariables.groups = np.array(list(range(StaticVariables.num_g)))
    StaticVariables.p_max = input_dict['p_max']
    StaticVariables.days = list(range(input_dict['d_max']))
    StaticVariables.periods = [np.array(
        list(range(StaticVariables.p_max))) for _ in range(len(StaticVariables.days))]

    for i in StaticVariables.days:
        StaticVariables.periods[i] = [j for j in range(StaticVariables.p_max)]

    x = StandardImplications()
    x.init_vars()
    x.basic_implications()
    x.correctness_implications()
    x.format_result()
    z = Parser([x.graph], [x.true_list])
    z.compute_result(1)

    return simple_ttable(z.result_graphs[0]['xtsgndp'][True])


def interface(input_dict):

    StaticVariables.duration = input_dict['duration']

    for (t, s, g, n) in list(StaticVariables.duration.keys()):
        StaticVariables.num_t = max([StaticVariables.num_t, t + 1])
        StaticVariables.num_s = max([StaticVariables.num_s, s + 1])
        StaticVariables.num_g = max([StaticVariables.num_g, g + 1])

    StaticVariables.teachers = np.array(list(range(StaticVariables.num_t)))
    StaticVariables.subjects = np.array(list(range(StaticVariables.num_s)))
    StaticVariables.groups = np.array(list(range(StaticVariables.num_g)))
    StaticVariables.p_max = input_dict['p_max']
    StaticVariables.days = list(range(input_dict['d_max']))
    StaticVariables.periods = [np.array(
        list(range(StaticVariables.p_max))) for _ in range(len(StaticVariables.days))]
    for i in StaticVariables.days:
        StaticVariables.periods[i] = [j for j in range(StaticVariables.p_max)]

    x = StandardImplications()
    x.init_vars()
    x.basic_implications()
    x.correctness_implications()
    x.format_result()
    y = ComfortImplications()
    print(input_dict['teacher_forbidden0'])
    print((not []))
    y.teacher_forbidden(teacher_forbidden0=input_dict['teacher_forbidden0'],
                        teacher_forbidden1=input_dict['teacher_forbidden1'],
                        teacher_forbidden2=input_dict['teacher_forbidden2'])
    print(y.comfort_true_list)

    y.teacher_requested(teacher_requested0=input_dict['teacher_requested0'],
                        teacher_requested1=input_dict['teacher_requested1'],
                        teacher_requested2=input_dict['teacher_requested2'])

    y.group_forbidden(group_forbidden0=input_dict['group_forbidden0'],
                      group_forbidden1=input_dict['group_forbidden1'],
                      group_forbidden2=input_dict['group_forbidden2'])

    y.group_requested(group_requested0=input_dict['group_requested0'],
                      group_requested1=input_dict['group_requested1'],
                      group_requested2=input_dict['group_requested2'])

    y.overlaps(teacher_overlap=input_dict['teacher_overlap'],
               teacher_no_overlap=input_dict['teacher_no_overlap'],
               group_no_overlap=input_dict['group_no_overlap'])

    y.teaching_days(teaching_days=input_dict['teaching_days'])

    y.duration(work_day_duration=input_dict['work_day_duration'],
               duration_upper_limit=input_dict['duration_upper_limit'],
               duration_lower_limit=input_dict['duration_lower_limit'])

    y.idle_duration(
        teacher_max_idle_length=input_dict['teacher_max_idle_length'],
        teacher_atmost_one_idle_period=input_dict['teacher_atmost_one_idle_period'],
        teacher_atmost_k_idle_period=input_dict['teacher_atmost_k_idle_period'],
        group_max_idle_length=input_dict['group_max_idle_length'],
        group_atmost_one_idle_period=input_dict['group_atmost_one_idle_period'],
        group_atmost_k_idle_period=input_dict['group_atmost_k_idle_period'])

    y.hour_specification(favoured_hours=input_dict['favoured_hours'],
                         last_first_hours=input_dict['last_first_hours'])

    y.non_consecutive(non_consecutive=input_dict['non_consecutive'])
    print(y.comfort_true_list)
    y.format_result()
    print(y.comfort_true_list)
    z = Parser([x.graph, y.comfort_graph], [x.true_list, y.comfort_true_list])
    z.compute_result(1)

    print(list(z.result_graphs.keys()))

    return simple_ttable(z.result_graphs[0]['xtsgndp'][True])
