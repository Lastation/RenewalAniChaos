import Function as f;

function main(cp)
{
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Goliath", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         var i = 50;
         var d = 25 + 25 * f.loop[cp];

         f.Table_Sin(cp, 45, 25);
         f.Table_Cos(cp, 45, 25);

         var x_i = f.CosAngle[cp];
         var y_i = f.SinAngle[cp];

         f.DoubleShape(cp, 1, "Vulture Spider Mine", d - i / 2 + x_i, d + i / 2 + y_i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", d - i, d + i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", d + 2 * x_i, d + 2 * y_i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", d + i, d - i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", d + i / 2 + x_i, d - i / 2 + y_i);

         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", d - i, d + i);
         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", d, d);
         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", d - i, d + i);

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "Vulture Spider Mine", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            f.DoubleShape(cp, 1, "60 + 1n Siege", d - i / 2 + x_i, d + i / 2 + y_i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", d - i, d + i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", d + 2 * x_i, d + 2 * y_i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", d + i, d - i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", d + i / 2 + x_i, d - i / 2 + y_i);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {

         var i = 50;
         var d = 25 + 25 * f.loop[cp];

         f.Table_Sin(cp, 45, 25);
         f.Table_Cos(cp, 45, 25);

         var x_i = f.CosAngle[cp];
         var y_i = f.SinAngle[cp];

         f.DoubleShape(cp, 1, "Vulture Spider Mine", -d + i / 2 - x_i, d + i / 2 + y_i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", -d + i, d + i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", -d - 2 * x_i, d + 2 * y_i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", -d - i, d - i);
         f.DoubleShape(cp, 1, "Vulture Spider Mine", -d - i / 2 - x_i, d - i / 2 + y_i);

         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", -d + i, d + i);
         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", -d, d);
         f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", -d + i, d + i);

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "Vulture Spider Mine", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            f.DoubleShape(cp, 1, "60 + 1n Siege", -d + i / 2 - x_i, d + i / 2 + y_i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", -d + i, d + i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", -d - 2 * x_i, d + 2 * y_i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", -d - i, d - i);
            f.DoubleShape(cp, 1, "60 + 1n Siege", -d - i / 2 - x_i, d - i / 2 + y_i);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 7)
         {
            var i = 50;
            var d = 150 - 25 * f.loop[cp];

            f.Table_Sin(cp, 45, 15);
            f.Table_Cos(cp, 45, 15);

            var x_i = f.CosAngle[cp];
            var y_i = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Guardian", d - i + x_i, d + i + y_i);
            f.SquareShape(cp, 1, "40 + 1n Guardian", d + 2 * x_i, d + 2 * y_i);
            f.SquareShape(cp, 1, "40 + 1n Guardian", d + i + x_i, d - i + y_i);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            if (f.loop[cp] == 1)
            {
               f.SquareShape(cp, 1, "40 + 1n Drone", d - i + x_i, d + i + y_i);
               f.SquareShape(cp, 1, "40 + 1n Drone", d + 2 * x_i, d + 2 * y_i);
               f.SquareShape(cp, 1, "40 + 1n Drone", d + i + x_i, d - i + y_i);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

            }
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 9)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         var i = 0;
         var x = 0;
         var y = 0;

         if (f.loop[cp] < 4)
         {
            i = f.loop[cp];

            if (i < 2)
            {
               x = 50 - 50 * i;
               y = 50 + 50 * i;
            }
            else
            {
               x = -50 - 50 * (i - 2);
               y = 50 - 50 * (i - 2); 
            }
         }
         else if (f.loop[cp] < 12)
         {
            i = f.loop[cp] - 4;

            if (i < 4)
            {
               x = 150 - 50 * i;
               y = 50 + 50 * i;
            }
            else
            {
               x = -50 - 50 * (i - 4);
               y = 150 - 50 * (i - 4); 
            }
         }

         if (i % 2 == 0 && f.loop[cp] < 12)
         {
            f.EdgeShapeAt(cp, 1, "Kakaru (Twilight)", 0, 2, 25, x, y);
            f.EdgeShapeAt(cp, 1, "Rhynadon (Badlands)", 0, 2, 25, x, y);
            f.EdgeShapeAt(cp, 1, "Kakaru (Twilight)", 0, 2, 25, -x, -y);
            f.EdgeShapeAt(cp, 1, "Rhynadon (Badlands)", 0, 2, 25, -x, -y);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);
         }
         else 
         {
            f.EdgeShapeAt(cp, 1, "40 + 1n Guardian", 0, 2, 25, x, y);
            f.EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 2, 25, x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.EdgeShapeAt(cp, 1, "40 + 1n Guardian", 0, 2, 25, -x, -y);
            f.EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 2, 25, -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 50, 50);

         }
         else if (f.loop[cp] == 1)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 50, 150);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 50, 150);

         }           
         else if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 150, 50);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 150, 50);
         }

         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 9)
         {
            f.Voice_Routine(cp, 21);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] < 6)
         {
            f.DoubleShape(cp, 1, "Protoss Dark Archon", 150 - 50 * f.loop[cp], 150);
            f.DoubleShape(cp, 1, "80 + 1n Tank", -150, 150 - 50 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);
         }

         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 45, 3, 75);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 45, 5, 150);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 22, 3, 75);
            f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 2, 100);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }
         else if (f.loop[cp] == 8)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3, 50);
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 3, 50);
            f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         else if (f.loop[cp] == 9)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 22, 3, 75);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }
         else if (f.loop[cp] == 12)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 22, 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 22, 3, 75);
            f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         else if (f.loop[cp] == 13)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 3, 100);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 15)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 26)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }

      else if (f.count[cp] == 6)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}