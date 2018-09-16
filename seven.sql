select shots.* from shots inner join shows on shots.ShowCode=shows.ShowCode where shows.CompanyName='CMP002' order by shots.BidPds;
