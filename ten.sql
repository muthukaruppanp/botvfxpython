select Artist as 'distinct Artists', (sum(HoursWorked)/sum(AssignedHours)) as Efficiency from assignments group by Artist;
