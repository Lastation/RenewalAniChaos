import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] < 3)
      {
         if (Bring(cp, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 3; i++)
            {
               MoveLocation(f.location[cp], "Zerg Devourer", cp, "Anywhere");
               RemoveUnitAt(1, "Zerg Devourer", "Anywhere", cp);

               if (i % 3 == 0) 
               {
                  f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                  f.SkillUnit(cp, 1, "130 + 1n Norad");
                  f.SkillUnit(cp, 1, "80 + 1n Tank");
               }
               else if (i % 3 == 1)
               {
                  f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                  f.SkillUnit(cp, 1, "40 + 1n Gantrithor");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
               else if (i % 3 == 2)
               {
                  f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                  f.SkillUnit(cp, 1, "40 + 1n Guardian");
                  f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               }

            }
            KillUnitAt(3, "60 + 1n Siege", "Anywhere", cp);
            KillUnitAt(3, "60 + 1n Danimoth", "Anywhere", cp);
            KillUnitAt(3, "60 + 1n Dragoon", "Anywhere", cp);
            KillUnitAt(3, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(3, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(3, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }
      }

      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            GiveUnits(All, "Zerg Devourer", P12, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P11, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P10, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P9, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P8, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P7, "Anywhere", cp);

            f.ShieldFix(cp, 1);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 11)
         {
            f.Voice_Routine(cp, 12);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 20)
         {
            f.Voice_Routine(cp, 13);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 62)
         {
            f.Voice_Routine(cp, 14);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 57)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P7);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P8);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P11);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P9);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P12);
         KillUnitAt(All, "Zerg Devourer", "Anywhere", P10);

         SetSwitch("JunkYardDog - Ekidona", Clear);
         SetSwitch("UiltimateSwitch", Clear);
         f.SkillEnd(cp);
      }

   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}