do_assignment = True
do_homework = True
absence = False

if do_assignment and do_homework and not absence:
    print('Good')
elif do_assignment or do_homework or absence:
    print('Normal')
else:
    print('Bad')