import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

var x = 0;
var y = 0;

function main(cp)
{
   MoveUnit(All, "40 + 1n Gantrithor", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 5)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] % 4 == 0)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var i = f.loop[cp] / 4;
            if (i % 4 == 0)
            {
               x = 50;
               y = 0;
            }
            else if (i % 4 == 1)
            {
               x = 50;
               y = 50;
            }
            else if (i % 4 == 2)
            {
               x = 0;
               y = 50;
            }
            else if (i % 4 == 2)
            {
               x = -50;
               y = 50;
            }

            f.DoubleShape(cp, 1, "60 + 1n Danimoth", x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
            f.DotShape(cp, 1, "40 + 1n Mojo", 0, 0);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");
         }

         if (f.loop[cp] >= 8 && f.loop[cp] < 12)
         {
            var i = f.loop[cp] - 8;

            var x = 225 - 75 * i;
            var y = 75 + 75 * i;

            f.SquareShape(cp, 1, "60 + 1n Siege", x, y);
            f.SquareShape(cp, 9, "Protoss Dark Archon", x, y);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 12)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 3, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] < 17)
         {
            var i = f.loop[cp] - 13;

            var x = 75 + 75 * i;
            var y = 225 - 75 * i;

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            f.SquareShape(cp, 4, "60 + 1n Archon", x, y);

            ModifyUnitHangarCount(1, All, "40 + 1n Gantrithor", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Gantrithor", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 24)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] % 4 == 0)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var i = f.loop[cp] / 4;
            if (i % 4 == 0)
            {
               x = -50;
               y = 0;
            }
            else if (i % 4 == 1)
            {
               x = -50;
               y = 50;
            }
            else if (i % 4 == 2)
            {
               x = 0;
               y = 50;
            }
            else if (i % 4 == 2)
            {
               x = 50;
               y = 50;
            }

            f.DoubleShape(cp, 1, "60 + 1n Danimoth", x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
            f.DotShape(cp, 1, "40 + 1n Mojo", 0, 0);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");
         }

         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 3, 100);
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3, 100);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         }
         if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 200);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 200);
            f.EdgeShape(cp, 1, "Protoss Reaver", 0, 5, 200);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Protoss Reaver", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 38)
         {
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 9 - 2 * f.loop[cp], 300 - 75 * f.loop[cp]);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n Siege", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n Siege", 200, 0);
            f.SquareShape(cp, 1, "60 + 1n Siege", 300, 0);
            f.SquareShape(cp, 1, "60 + 1n Siege", 300, 300);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 300, 200);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 200, 300);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 300);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 200);
            f.SquareShape(cp, 1, "50 + 1n Tank", 300, 100);
         }

         if (f.loop[cp] == 10)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 75);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 3, 75);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         }
         if (f.loop[cp] == 12)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 125);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 3, 125);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

         }
         if (f.loop[cp] == 14)
         {
            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 125);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 3, 125);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SquareShapeAt(cp, 1, "60 + 1n Danimoth", 32, 32, 40, 100);
            f.SquareShapeAt(cp, 1, "Protoss Dark Archon", 32, 32, 40, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 16)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SquareShapeAt(cp, 1, "60 + 1n Danimoth", 32, 32, -40, 100);
            f.SquareShapeAt(cp, 1, "Protoss Dark Archon", 32, 32, -40, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 18)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SquareShapeAt(cp, 1, "60 + 1n Danimoth", 32, 32, 100, 100);
            f.SquareShapeAt(cp, 1, "Protoss Dark Archon", 32, 32, 100, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 22)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }

         if (f.loop[cp] >= 23)
         {
            if (f.loop[cp] == 23) { x = 100; y = 0; }
            if (f.loop[cp] == 24) { x = 100; y = 100; }
            if (f.loop[cp] == 25) { x = 200; y = -100; }
            if (f.loop[cp] == 26) { x = 200; y = 0; }
            if (f.loop[cp] == 27) { x = 200; y = 100; }
            if (f.loop[cp] == 28) { x = 200; y = 200; }

            if (f.loop[cp] % 2 == 1)
            {
               EdgeShapeAt(cp, 1, "60 + 1n Dragoon", 45, 0, 50, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 45, 0, 50, x, y);
            }
            if (f.loop[cp] % 2 == 0)
            {
               EdgeShapeAt(cp, 1, "50 + 1n Tank", 45, 0, 50, x, y);
               EdgeShapeAt(cp, 1, "Protoss Dark Archon", 45, 0, 50, x, y);
            }

            EdgeShapeAt(cp, 1, "40 + 1n Gantrithor", 45, 0, 50, x, y);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);

         }
         if (f.loop[cp] == 29)
         {
            f.NxNSquareShapeAt(cp, 1, "60 + 1n Danimoth", 3, 50, 200, 200);
            f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 50, 200, 200);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 33)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.NxNSquareShapeAt(cp, 1, "60 + 1n Danimoth", 3, 50, 0, 200);
            f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 50, 0, 200);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 37)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 38)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y)
{
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, x, y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -x, -y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -y, x);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, y, -x);
}