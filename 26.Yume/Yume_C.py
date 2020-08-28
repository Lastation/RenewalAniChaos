import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {                        
            f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 0, 3, 50);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3, 50);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {                        
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
            f.EdgeShape(cp, 1, "40 + 1n Marine", 0, 3, 100);
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 5, 100);
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 2)
         {         
            var x = 0;
            var y = 0;

            if (f.loop[cp] == 0) { x = 150; y = 100; }
            else if (f.loop[cp] == 1) { x = 100; y = 50; }

            f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
            f.SquareShape(cp, 1, "40 + 1n Guardian", y, x);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;

         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 50);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;

         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 50);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;

         }

      }
      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}