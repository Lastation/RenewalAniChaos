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
         if (f.loop[cp] < 2)
         {         
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 80);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 160);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 3)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(heroID, 1, "40 + 1n Wraith", location, cp, 3, 75);
            f.NxNSquareShape(heroID, 1, "50 + 1n Tank", location, cp, 3, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 4)
         {
            f.NxNSquareShape(heroID, 1, "40 + 1n Wraith", location, cp, 5, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 5)
         {
            f.NxNSquareShape(heroID, 1, "40 + 1n Guardian", location, cp, 5, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 160);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.NxNSquareShape(heroID, 1, "Kakaru (Twilight)", location, cp, 5, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillLoop");


         }
         if (f.loop[cp] == 1)
         {         
            f.NxNSquareShape(heroID, 1, " Unit. Hoffnung 25000", location, cp, 5, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

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