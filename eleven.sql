select ShotID ,(sum(HoursWorked)/sum(AssignedHours)) as ShotEfficiency from assignments group by ShotID;
