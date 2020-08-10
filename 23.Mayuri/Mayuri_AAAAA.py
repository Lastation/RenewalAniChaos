import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.HoldPosition(cp);
   MoveLocation("23.Mayuri_Bozo", f.heroID[cp], cp, "Anywhere");
   MoveUnit(All, "50 + 1n Battlecruiser", cp, "Anywhere", "[Skill]HoldPosition");
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 12)
         {    
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            GiveUnits(All, "60 + 3n Siege", P9, "Anywhere", cp);
            SetSwitch("Recall - Mayuri", Set);

            KillUnitAt(10, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {       
            f.Voice_Routine(cp, 14);

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 36)
         {    
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "80 + 1n Vulture", 7, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Vulture", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 36)
         {       
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);
            KillUnitAt(All, "60 + 3n Siege", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
         SetSwitch("Recall - Mayuri", Clear);
         SetSwitch("UiltimateSwitch", Clear);
         f.SkillEnd(cp);
      }
   }
}