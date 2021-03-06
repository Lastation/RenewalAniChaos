import Function as f;

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         var x = 0;
         var y = 0;

         if (f.loop[cp] == 0) { x = 50; y = 50; }
         else if (f.loop[cp] == 1) { x = 0; y = 50; }
         else if (f.loop[cp] == 2) { x = -50; y = 50; }
         else if (f.loop[cp] == 3) { x = -50; y = 0; }

         f.DoubleShape(cp, 1, "40 + 1n Mojo", x, y);
         f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         f.DoubleShape(cp, 1, "Kakaru (Twilight)", -y, x);
         f.DoubleShape(cp, 1, "Rhynadon (Badlands)", -y, x);
         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         }

         if (f.loop[cp] < 4)
         {
            var d = 50 + 50 * (f.loop[cp] % 4);

            f.SquareShape(cp, 1, "40 + 1n Guardian", d, d);
            f.SquareShape(cp, 1, "60 + 1n Archon", d, d);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] < 8)
         {
            var d = 200 - 50 * (f.loop[cp] % 4);

            f.SquareShape(cp, 1, "40 + 1n Guardian", d, d);
            f.SquareShape(cp, 1, "60 + 1n Archon", d, d);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         if (f.loop[cp] < 8 && f.loop[cp] % 2 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            var x = 0;
            var y = 0;

            if (f.loop[cp] / 2 % 2 == 0) { x = 50; y = 50; }
            else if (f.loop[cp] / 2 % 2 == 1) { x = 0; y = 50; }

            f.SquareShape(cp, 1, "Bengalaas (Jungle)", -y, x);
            f.SquareShape(cp, 1, "Target", -y, x);
            f.SquareShape(cp, 1, "40 + 1n Wraith", x, y);
            f.SquareShape(cp, 1, "Scantid (Desert)", x, y);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);

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
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 50);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 3, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] >= 2 && f.loop[cp] < 6)
         {
            var i = (f.loop[cp] - 2);

            f.SquareShape(cp, 1, "40 + 1n Guardian", -100 + 50 * i, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", -100 + 50 * i, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         if (f.loop[cp] == 2)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 50);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Mojo", 3, 50);

            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}