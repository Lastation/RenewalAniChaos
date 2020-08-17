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
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 50);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 50);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 50);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 50);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 50, 50);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.SquareShape(cp, 1, "Protoss Dark Templar", 120 - 30 * f.loop[cp], 30 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.SquareShape(cp, 1, "40 + 1n Zealot", 120, 0);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 80, 40);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 40, 80);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.SquareShape(cp, 1, "60 + 1n High Templar", 120, 0);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 120, 0);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n High Templar", 80, 40);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 80, 40);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n High Templar", 40, 80);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 40, 80);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

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