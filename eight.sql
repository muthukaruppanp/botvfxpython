select DISTINCT assignments.Artist from shots inner join shows on shots.ShowCode=shows.ShowCode inner join assignments on shots.ShotID = assignments.ShotID where shows.CompanyName='CMP002';
