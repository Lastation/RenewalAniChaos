import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 50);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 5, 100);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 5, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 50, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 0, 50);

            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 0, 50);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 0, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 0, 50);

            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 50, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 0, 50);

            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 10)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 0, 50);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 0, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 0, 50);

            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }

         if ((f.loop[cp] % 8) / 4 == 0)
         {
            f.DoubleShape(cp, 1, "Rhynadon (Badlands)", 100 - 50 * (f.loop[cp] % 4), 100);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);
         }
         else if ((f.loop[cp] % 8) / 4 == 1)
         {
            f.DoubleShape(cp, 1, "Rhynadon (Badlands)", -100, 100 - 50 * (f.loop[cp] % 4));
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 5, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 4)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         else if (f.loop[cp] == 6)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 50);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
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
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}