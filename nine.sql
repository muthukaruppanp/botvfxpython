select shows.CompanyName,shows.ShowCode,shots.ShotID,shots.ShotName,shots.BidPds,assignments.Artist,assignments.AssignedHours,assignments.HoursWorked from shows join shots join assignments;
