import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 50);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n High Templar", 150, 100);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 150, 100);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 150);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 4, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Goliath", 100, 100 - 50 * f.loop[cp]);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 100 - 50 * f.loop[cp]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

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