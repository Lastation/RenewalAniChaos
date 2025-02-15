import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 3, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Mojo", 0, 5, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 150);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 1280);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 50);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 50, 100);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 50);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 100);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 100);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "Target", 45, 3, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Marine", 45, 3, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 120, 30);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 120, -30);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 120, 30);
            f.SquareShape(cp, 1, "50 + 1n Tank", 120, -30);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "Target", 0, 3, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Marine", 0, 3, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         
         else if (f.loop[cp] == 6)
         {         
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

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