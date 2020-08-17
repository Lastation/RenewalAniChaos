import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {         
            f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 50 * f.loop[cp], 100);
            f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 50 * f.loop[cp], -100);
            f.DotShape(cp, 1, "40 + 1n Zealot", -100, 100 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", 100, -100 + 50 * f.loop[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 100);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.SquareShape(cp, 1, "Protoss Dark Templar", 50, 0);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SquareShape(cp, 1, "40 + 1n Zealot", 50, 50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.SquareShape(cp, 1, "Protoss Dark Templar", 100, 0);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 100);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 0);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 0);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
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
         else if (f.loop[cp] == 7)
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