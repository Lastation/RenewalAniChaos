import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         if (f.loop[cp] % 4 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            if ((f.loop[cp] % 8) / 4 == 0)
               f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 150);
            else
               f.SquareShapeWithProperty(cp, 1, "40 + 1n Guardian", 150, 150, 1);

            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] % 4 == 2)
         {
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 150);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         if (f.loop[cp] < 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 32 - 32 * f.loop[cp], 64);
            f.SquareShape(cp, 1, "Rhynadon (Badlands)", 32 - 32 * f.loop[cp], 64);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Ghost", 96, 96);
            f.SquareShape(cp, 1, "Target", 96, 96);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            f.SquareShape(cp, 1, "Target", 32, 32);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n Siege", 96, 96);
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 96, 96);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         if (f.loop[cp] % 4 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            if ((f.loop[cp] % 8) / 4 == 0)
               f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 150);
            else
               f.SquareShapeWithProperty(cp, 1, "40 + 1n Guardian", 150, 150, 1);

            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] % 4 == 2)
         {
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 150);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         if (f.loop[cp] < 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 16 + 16 * f.loop[cp], 64 - 16 * f.loop[cp]);
            f.SquareShape(cp, 1, "Rhynadon (Badlands)", 16 + 16 * f.loop[cp], 64 - 16 * f.loop[cp]);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Ghost", 128, 0);
            f.SquareShape(cp, 1, "Target", 128, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            f.SquareShape(cp, 1, "Target", 40, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n Siege", 128, 0);
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 128, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
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
         if (f.loop[cp] % 2 == 0)
         {
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            if ((f.loop[cp] % 4) / 2 == 0)
               f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 45, 3, 50);
            else
               f.EdgeShapeWithProperty(cp, 1, "40 + 1n Mutalisk", 45, 3, 50, 1);

            f.EdgeShape(cp, 1, "Rhynadon (Badlands)", 45, 3, 50);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            f.SquareShape(cp, 1, "Scantid (Desert)", 100, 100);
            KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);

            if ((f.loop[cp] % 4) / 2 == 0)
            {
               f.SquareShape(cp, 1, "60 + 1n Archon", 50 - 50 * (f.loop[cp] % 2), 50 * (f.loop[cp] % 2));
               f.SquareShape(cp, 1, "Kakaru (Twilight)", 50 - 50 * (f.loop[cp] % 2), 50 * (f.loop[cp] % 2));
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
               KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            }
            else if ((f.loop[cp] % 4) / 2 == 1)
            {
               f.SquareShape(cp, 1, "60 + 1n Archon", 0 - 50 * (f.loop[cp] % 2), 50 * (f.loop[cp] % 2));
               f.SquareShape(cp, 1, "Kakaru (Twilight)", 0 - 50 * (f.loop[cp] % 2), 50 * (f.loop[cp] % 2));
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
               KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            }
         }

         if (f.loop[cp] % 4 == 0)
         {
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            if ((f.loop[cp] % 8) / 4 == 0)
               f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 150);
            else
               f.SquareShapeWithProperty(cp, 1, "40 + 1n Guardian", 150, 150, 1);

            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] % 4 == 2)
         {
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 150);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);


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

            x = 120 - 40 * i;
            y = 40 + 40 * i;
         }
         else if (f.loop[cp] == 4)
         {
            x = 80;
            y = 0;
         }
         else if (f.loop[cp] == 5)
         {
            x = 80;
            y = 80;
         }
         else if (f.loop[cp] == 6 || f.loop[cp] == 7)
         {
            x = 150;
            y = 150;
         }

         if (f.loop[cp] < 8)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SquareShape(cp, 1, "80 + 1n Guardian", x, y);
            EdgeShapeAt(cp, 1, "Bengalaas (Jungle)", 0, 2, 25, x, y);

            KillUnitAt(All, "80 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         }


         if (f.loop[cp] == 8)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 160, 0);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 120, 40);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 80, 80);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 40, 120);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 80, 0);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 160, 0);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 120, 40);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 80, 80);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 40, 120);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 80, 0);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 12)
         {
            f.SquareShapeAt(cp, 1, "40 + 1n Guardian", 25, 25, 150, 150);
            f.SquareShapeAt(cp, 1, "40 + 1n Guardian", 25, 25, -150, -150);
            f.SquareShapeAt(cp, 1, "40 + 1n Guardian", 25, 25, -150, 150);
            f.SquareShapeAt(cp, 1, "40 + 1n Guardian", 25, 25, 150, -150);

            f.SquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 25, 25, 150, 150);
            f.SquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 25, 25, -150, -150);
            f.SquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 25, 25, -150, 150);
            f.SquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 25, 25, 150, -150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

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