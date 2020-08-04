import Function as f;

const s = StringBuffer();

function main(cp, location, heroID)
{
   f.loop[cp] = dwread_epd(212 * 12 + cp);
   f.count[cp]  = dwread_epd(181 * 12 + cp);

   if (Deaths(cp, Exactly, 0, " `WaitTime"))
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {                        
            f.LineShape(heroID, 1, "Kakaru (Twilight)", location, cp, 45 * 3 * f.loop[cp], 7, 50, 50);
            f.LineShape(heroID, 1, "Protoss Dark Templar", location, cp, 45 * 3 * f.loop[cp], 7, 50, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 0);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }
      if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 3)
         {    
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 50);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 3)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(heroID, 1, " Unit. Hoffnung 25000", location, cp, 3, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 0);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }

      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}