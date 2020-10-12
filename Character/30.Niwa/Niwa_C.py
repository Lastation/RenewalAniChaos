import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 3, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 3, 100);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 3, 100);

            f.EdgeShape(cp, 1, "Target", 45, 3, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 3, 50);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 3, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 3, 100);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 8)
         {
            RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", cp);

            f.MoveLoc("40 + 1n Drone", cp, 0, 0);
            RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", cp);
            f.SkillUnit(cp, 1, "40 + 1n Mojo");

            if (f.loop[cp] % 2 == 0)
            {
               f.SkillUnit(cp, 1, "60 + 1n Archon");
            }
            else if (f.loop[cp] % 2 == 1)
            {
               f.SkillUnit(cp, 1, "Protoss Dark Archon");
            }

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);


            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}